import DailyGame from '@/components/DailyGame'
import { Game } from '@/types/games'

export default async function DailyGamePage() {
  const data = await getData()

  return <DailyGame question={data.question} />
}

async function getData(): Promise<Game> {
  const res = await fetch('http://localhost:8000/games/daily')

  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }

  return res.json()
}
