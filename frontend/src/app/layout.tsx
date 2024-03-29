import type { Metadata } from 'next'
import './globals.css'
import Providers from '@/components/Providers'
import Menu from '@/components/Menu'

export const metadata: Metadata = {
  title: 'Chicane Game',
  description: 'Generated by create next app',
}

export const revalidate = 60

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body>
        <Providers
          attribute="class"
          defaultTheme="dark"
          enableSystem
          disableTransitionOnChange
        >
          <div className="flex flex-col h-screen">
            <header className="w-full py-4 px-6 flex justify-between items-center">
              <div>Chicane Game</div>
              <Menu />
            </header>
            {children}
          </div>
        </Providers>
      </body>
    </html>
  )
}
