import { getDailyGame } from '@/api/games'
import DailyGame from '@/components/DailyGame'

export default async function DailyGamePage() {
  // TODO: Add error case
  const data = await getDailyGame()

  return <DailyGame question={data.question} categoryId={data.category_id} />
}
