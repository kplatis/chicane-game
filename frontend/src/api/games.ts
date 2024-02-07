import { Game } from '@/types/games'

export async function getDailyGame(): Promise<Game> {
  const res = await fetch('http://localhost:8000/games/daily')
  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }

  return res.json()
}
