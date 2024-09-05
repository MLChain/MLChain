import { useReactFlow } from 'reactflow'
import { useKeyPress } from 'ahooks'
import { useCallback } from 'react'
import {
  getKeyboardKeyCodeBySystem,
  isEventTargetInputArea,
} from '../utils'
import { useWorkflowHistoryStore } from '../workflow-history-store'
import { useWorkflowStore } from '../store'
import {
  useEdgesInteractions,
  useNodesInteractions,
  useNodesSyncDraft,
  useWorkflowMoveMode,
  useWorkflowOrganize,
  useWorkflowStartRun,
} from '.'

export const useShortcuts = (): void => {
  const {
    handleNodesCopy,
    handleNodesPaste,
    handleNodesDuplicate,
    handleNodesDelete,
    handleHistoryBack,
    handleHistoryForward,
  } = useNodesInteractions()
  const { handleStartWorkflowRun } = useWorkflowStartRun()
  const { shortcutsEnabled: workflowHistoryShortcutsEnabled } = useWorkflowHistoryStore()
  const { handleSyncWorkflowDraft } = useNodesSyncDraft()
  const { handleEdgeDelete } = useEdgesInteractions()
  const workflowStore = useWorkflowStore()
  const {
    handleModeHand,
    handleModePointer,
  } = useWorkflowMoveMode()
  const { handleLayout } = useWorkflowOrganize()

  const {
    zoomIn,
    zoomOut,
    zoomTo,
    fitView,
  } = useReactFlow()

  const shouldHandleShortcut = useCallback((e: KeyboardEvent) => {
    const { showFeaturesPanel } = workflowStore.getState()
    return !showFeaturesPanel && !isEventTargetInputArea(e.target as HTMLElement)
  }, [workflowStore])

  useKeyPress(['delete', 'backspace'], (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      handleNodesDelete()
      handleEdgeDelete()
    }
  })

  useKeyPress(`${getKeyboardKeyCodeBySystem('ctrl')}.c`, (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      handleNodesCopy()
    }
  }, { exactMatch: true, useCapture: true })

  useKeyPress(`${getKeyboardKeyCodeBySystem('ctrl')}.v`, (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      handleNodesPaste()
    }
  }, { exactMatch: true, useCapture: true })

  useKeyPress(`${getKeyboardKeyCodeBySystem('ctrl')}.d`, (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      handleNodesDuplicate()
    }
  }, { exactMatch: true, useCapture: true })

  useKeyPress(`${getKeyboardKeyCodeBySystem('alt')}.r`, (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      handleStartWorkflowRun()
    }
  }, { exactMatch: true, useCapture: true })

  useKeyPress(`${getKeyboardKeyCodeBySystem('ctrl')}.z`, (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      workflowHistoryShortcutsEnabled && handleHistoryBack()
    }
  }, { exactMatch: true, useCapture: true })

  useKeyPress(
    [`${getKeyboardKeyCodeBySystem('ctrl')}.y`, `${getKeyboardKeyCodeBySystem('ctrl')}.shift.z`],
    (e) => {
      if (shouldHandleShortcut(e)) {
        e.preventDefault()
        workflowHistoryShortcutsEnabled && handleHistoryForward()
      }
    },
    { exactMatch: true, useCapture: true },
  )

  useKeyPress('h', (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      handleModeHand()
    }
  }, {
    exactMatch: true,
    useCapture: true,
  })

  useKeyPress('v', (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      handleModePointer()
    }
  }, {
    exactMatch: true,
    useCapture: true,
  })

  useKeyPress(`${getKeyboardKeyCodeBySystem('ctrl')}.o`, (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      handleLayout()
    }
  }, { exactMatch: true, useCapture: true })

  useKeyPress(`${getKeyboardKeyCodeBySystem('ctrl')}.1`, (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      fitView()
      handleSyncWorkflowDraft()
    }
  }, {
    exactMatch: true,
    useCapture: true,
  })

  useKeyPress('shift.1', (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      zoomTo(1)
      handleSyncWorkflowDraft()
    }
  }, {
    exactMatch: true,
    useCapture: true,
  })

  useKeyPress('shift.5', (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      zoomTo(0.5)
      handleSyncWorkflowDraft()
    }
  }, {
    exactMatch: true,
    useCapture: true,
  })

  useKeyPress(`${getKeyboardKeyCodeBySystem('ctrl')}.dash`, (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      zoomOut()
      handleSyncWorkflowDraft()
    }
  }, {
    exactMatch: true,
    useCapture: true,
  })

  useKeyPress(`${getKeyboardKeyCodeBySystem('ctrl')}.equalsign`, (e) => {
    if (shouldHandleShortcut(e)) {
      e.preventDefault()
      zoomIn()
      handleSyncWorkflowDraft()
    }
  }, {
    exactMatch: true,
    useCapture: true,
  })
}
