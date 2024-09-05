'use client'
import type { FC } from 'react'
import React, { useCallback } from 'react'
import { useBoolean } from 'ahooks'
import {
  RiDeleteBinLine,
  RiEditLine,
} from '@remixicon/react'
import type { DataSet } from '@/models/datasets'
import { DataSourceType } from '@/models/datasets'
import FileIcon from '@/app/components/base/file-icon'
import { Folder } from '@/app/components/base/icons/src/vender/solid/files'
import SettingsModal from '@/app/components/app/configuration/dataset-config/settings-modal'
import Drawer from '@/app/components/base/drawer'
import useBreakpoints, { MediaType } from '@/hooks/use-breakpoints'
import Badge from '@/app/components/base/badge'
import { useKnowledge } from '@/hooks/use-knowledge'

type Props = {
  payload: DataSet
  onRemove: () => void
  onChange: (dataSet: DataSet) => void
  readonly?: boolean
}

const DatasetItem: FC<Props> = ({
  payload,
  onRemove,
  onChange,
  readonly,
}) => {
  const media = useBreakpoints()
  const isMobile = media === MediaType.mobile
  const { formatIndexingTechniqueAndMethod } = useKnowledge()

  const [isShowSettingsModal, {
    setTrue: showSettingsModal,
    setFalse: hideSettingsModal,
  }] = useBoolean(false)

  const handleSave = useCallback((newDataset: DataSet) => {
    onChange(newDataset)
    hideSettingsModal()
  }, [hideSettingsModal, onChange])

  return (
    <div className='flex items-center h-10 justify-between rounded-xl px-2 bg-white border border-gray-200  cursor-pointer group/dataset-item'>
      <div className='w-0 grow flex items-center space-x-1.5'>
        {
          payload.data_source_type === DataSourceType.NOTION
            ? (
              <div className='shrink-0 flex items-center justify-center w-6 h-6 rounded-md border-[0.5px] border-[#EAECF5]'>
                <FileIcon type='notion' className='w-4 h-4' />
              </div>
            )
            : <div className='shrink-0 flex items-center justify-center w-6 h-6 bg-[#F5F8FF] rounded-md border-[0.5px] border-[#E0EAFF]'>
              <Folder className='w-4 h-4 text-[#444CE7]' />
            </div>
        }
        <div className='w-0 grow text-[13px] font-normal text-gray-800 truncate'>{payload.name}</div>
      </div>
      {!readonly && (
        <div className='hidden group-hover/dataset-item:flex shrink-0 ml-2  items-center space-x-1'>
          <div
            className='flex items-center justify-center w-6 h-6 hover:bg-black/5 rounded-md cursor-pointer'
            onClick={showSettingsModal}
          >
            <RiEditLine className='w-4 h-4 text-gray-500' />
          </div>
          <div
            className='flex items-center justify-center w-6 h-6 hover:bg-black/5 rounded-md cursor-pointer'
            onClick={onRemove}
          >
            <RiDeleteBinLine className='w-4 h-4 text-gray-500' />
          </div>
        </div>
      )}
      <Badge
        className='group-hover/dataset-item:hidden shrink-0'
        text={formatIndexingTechniqueAndMethod(payload.indexing_technique, payload.retrieval_model_dict?.search_method)}
      />

      {isShowSettingsModal && (
        <Drawer isOpen={isShowSettingsModal} onClose={hideSettingsModal} footer={null} mask={isMobile} panelClassname='mt-16 mx-2 sm:mr-2 mb-3 !p-0 !max-w-[640px] rounded-xl'>
          <SettingsModal
            currentDataset={payload}
            onCancel={hideSettingsModal}
            onSave={handleSave}
          />
        </Drawer>
      )}
    </div>
  )
}
export default React.memo(DatasetItem)
