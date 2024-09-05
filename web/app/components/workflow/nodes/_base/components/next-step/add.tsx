import {
  memo,
  useCallback,
} from 'react'
import { useTranslation } from 'react-i18next'
import {
  RiAddLine,
} from '@remixicon/react'
import {
  useAvailableBlocks,
  useNodesInteractions,
  useNodesReadOnly,
} from '@/app/components/workflow/hooks'
import BlockSelector from '@/app/components/workflow/block-selector'
import type {
  CommonNodeType,
  OnSelectBlock,
} from '@/app/components/workflow/types'

type AddProps = {
  nodeId: string
  nodeData: CommonNodeType
  sourceHandle: string
  branchName?: string
}
const Add = ({
  nodeId,
  nodeData,
  sourceHandle,
  branchName,
}: AddProps) => {
  const { t } = useTranslation()
  const { handleNodeAdd } = useNodesInteractions()
  const { nodesReadOnly } = useNodesReadOnly()
  const { availableNextBlocks } = useAvailableBlocks(nodeData.type, nodeData.isInIteration)

  const handleSelect = useCallback<OnSelectBlock>((type, toolDefaultValue) => {
    handleNodeAdd(
      {
        nodeType: type,
        toolDefaultValue,
      },
      {
        prevNodeId: nodeId,
        prevNodeSourceHandle: sourceHandle,
      },
    )
  }, [nodeId, sourceHandle, handleNodeAdd])

  const renderTrigger = useCallback((open: boolean) => {
    return (
      <div
        className={`
          relative flex items-center px-2 h-9 rounded-lg border border-dashed border-divider-regular bg-dropzone-bg
          hover:bg-dropzone-bg-hover text-xs text-text-placeholder cursor-pointer
          ${open && '!bg-components-dropzone-bg-alt'}
          ${nodesReadOnly && '!cursor-not-allowed'}
        `}
      >
        {
          branchName && (
            <div
              className='absolute left-1 right-1 -top-[7.5px] flex items-center h-3 text-[10px] text-text-placeholder font-semibold'
              title={branchName.toLocaleUpperCase()}
            >
              <div className='inline-block px-0.5 rounded-[5px] bg-background-default truncate'>{branchName.toLocaleUpperCase()}</div>
            </div>
          )
        }
        <div className='flex items-center justify-center mr-1.5 w-5 h-5 rounded-[5px] bg-background-default-dimm'>
          <RiAddLine className='w-3 h-3' />
        </div>
        {t('workflow.panel.selectNextStep')}
      </div>
    )
  }, [branchName, t, nodesReadOnly])

  return (
    <BlockSelector
      disabled={nodesReadOnly}
      onSelect={handleSelect}
      placement='top'
      offset={0}
      trigger={renderTrigger}
      popupClassName='!w-[328px]'
      availableBlocksTypes={availableNextBlocks}
    />
  )
}

export default memo(Add)
