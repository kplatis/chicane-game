'use client'

import { getOptionsByCategoryId } from '@/api/categories'
import { useQuery } from 'react-query'
import Spinner from '../Spinner'
import { Label } from '@/components/ui/label'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { Option } from '@/types/categories'

type GameOptionsProps = {
  categoryId: number
}

export default function GameOptions({ categoryId }: GameOptionsProps) {
  const { data, isLoading, isError } = useQuery<Option[], Error>(
    ['options', categoryId],
    () => getOptionsByCategoryId(categoryId),
  )

  if (isLoading) {
    return <Spinner />
  }
  if (data) {
    return (
      <form>
        <div className="grid w-full items-center gap-4">
          <div className="flex flex-col space-y-1.5">
            <Label htmlFor="framework">Framework</Label>
            <Select>
              <SelectTrigger id="framework">
                <SelectValue placeholder="Select" />
              </SelectTrigger>
              <SelectContent position="popper">
                {data.map((option) => (
                  <SelectItem key={option.id} value={option.title}>
                    {option.title}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
        </div>
      </form>
    )
  }
  return
}
