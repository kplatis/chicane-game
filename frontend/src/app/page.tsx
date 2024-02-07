import Menu from '@/components/Menu'
import RootLayout from './layout'

export default function Home({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <main>
      <RootLayout>
        <Menu />
        {children}
      </RootLayout>
    </main>
  )
}
