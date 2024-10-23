import type { FC } from 'react'
import {
  memo,
  useCallback,
  useMemo,
} from 'react'
import type { ModelAndParameter } from '../types'
import {
  APP_CHAT_WITH_MULTIPLE_MODEL,
  APP_CHAT_WITH_MULTIPLE_MODEL_RESTART,
} from '../types'
import {
  useConfigFromDebugContext,
  useFormattingChangedSubscription,
} from '../hooks'
import Chat from '@/app/components/base/chat/chat'
import { useChat } from '@/app/components/base/chat/chat/hooks'
import { useDebugConfigurationContext } from '@/context/debug-configuration'
import type { OnSend } from '@/app/components/base/chat/types'
import { useEventEmitterContextContext } from '@/context/event-emitter'
import { useProviderContext } from '@/context/provider-context'
import {
  fetchConversationMessages,
  fetchSuggestedQuestions,
  stopChatMessageResponding,
} from '@/service/debug'
import Avatar from '@/app/components/base/avatar'
import { useAppContext } from '@/context/app-context'
import { ModelFeatureEnum } from '@/app/components/header/account-setting/model-provider-page/declarations'

type ChatItemProps = {
  modelAndParameter: ModelAndParameter
}
const ChatItem: FC<ChatItemProps> = ({
  modelAndParameter,
}) => {
  const { userProfile } = useAppContext()
  const {
    modelConfig,
    appId,
    inputs,
    visionConfig,
    collectionList,
  } = useDebugConfigurationContext()
  const { textGenerationModelList } = useProviderContext()
  const config = useConfigFromDebugContext()
  const {
    chatList,
    chatListRef,
    isResponding,
    handleSend,
    suggestedQuestions,
    handleRestart,
  } = useChat(
    config,
    {
      inputs,
      promptVariables: modelConfig.configs.prompt_variables,
    },
    [],
    taskId => stopChatMessageResponding(appId, taskId),
  )
  useFormattingChangedSubscription(chatList)

  const doSend: OnSend = useCallback((message, files) => {
    const currentProvider = textGenerationModelList.find(item => item.provider === modelAndParameter.provider)
    const currentModel = currentProvider?.models.find(model => model.model === modelAndParameter.model)
    const supportVision = currentModel?.features?.includes(ModelFeatureEnum.vision)

    const configData = {
      ...config,
      model: {
        provider: modelAndParameter.provider,
        name: modelAndParameter.model,
        mode: currentModel?.model_properties.mode,
        completion_params: modelAndParameter.parameters,
      },
    }

    const data: any = {
      query: message,
      inputs,
      model_config: configData,
      parent_message_id: chatListRef.current.at(-1)?.id || null,
    }

    if (visionConfig.enabled && files?.length && supportVision)
      data.files = files

    handleSend(
      `apps/${appId}/chat-messages`,
      data,
      {
        onGetConversationMessages: (conversationId, getAbortController) => fetchConversationMessages(appId, conversationId, getAbortController),
        onGetSuggestedQuestions: (responseItemId, getAbortController) => fetchSuggestedQuestions(appId, responseItemId, getAbortController),
      },
    )
  }, [appId, config, handleSend, inputs, modelAndParameter, textGenerationModelList, visionConfig.enabled, chatListRef])

  const { eventEmitter } = useEventEmitterContextContext()
  eventEmitter?.useSubscription((v: any) => {
    if (v.type === APP_CHAT_WITH_MULTIPLE_MODEL)
      doSend(v.payload.message, v.payload.files)
    if (v.type === APP_CHAT_WITH_MULTIPLE_MODEL_RESTART)
      handleRestart()
  })

  const allToolIcons = useMemo(() => {
    const icons: Record<string, any> = {}
    modelConfig.agentConfig.tools?.forEach((item: any) => {
      icons[item.tool_name] = collectionList.find((collection: any) => collection.id === item.provider_id)?.icon
    })
    return icons
  }, [collectionList, modelConfig.agentConfig.tools])

  if (!chatList.length)
    return null

  return (
    <Chat
      config={config}
      chatList={chatList}
      isResponding={isResponding}
      noChatInput
      noStopResponding
      chatContainerClassName='p-4'
      chatFooterClassName='p-4 pb-0'
      suggestedQuestions={suggestedQuestions}
      onSend={doSend}
      showPromptLog
      questionIcon={<Avatar name={userProfile.name} size={40} />}
      allToolIcons={allToolIcons}
      hideLogModal
      noSpacing
    />
  )
}

export default memo(ChatItem)
