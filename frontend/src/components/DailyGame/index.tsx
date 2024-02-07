import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import GameOptions from './GameOptions'

type DailyGameProps = {
  question: string
  categoryId: number
}

export default function DailyGame({ question, categoryId }: DailyGameProps) {
  return (
    <Card className="w-[350px]">
      <CardHeader>
        <CardTitle className="text-center">{question}</CardTitle>
      </CardHeader>
      <CardContent>
        <GameOptions categoryId={categoryId} />
      </CardContent>
    </Card>
  )
}
