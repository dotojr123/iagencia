export const metadata = {
  title: 'Jules AI Agency',
  description: 'Autonomous AI Agency Dashboard',
}

import './globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
