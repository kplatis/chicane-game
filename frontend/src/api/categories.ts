import { Option } from '@/types/categories'

export async function getOptionsByCategoryId(
  categoryId: number,
): Promise<Option[]> {
  const options = await fetch(
    `http://localhost:8000/categories/${categoryId}/options`,
  )

  if (!options.ok) {
    throw new Error('Failed to fetch data')
  }

  return options.json()
}
