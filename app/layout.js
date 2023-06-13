import './globals.css'
import NavBar from "./components/navbar"

export const metadata = {
  title: 'Craftsy',
  description: 'E-commerce site for Craftsy'
}

export default async function RootLayout({ children, onSetUser }) {
  return (
    <html lang="en">
      <body>
      <nav>
          <NavBar />
        </nav>
        {children}
      </body>
    </html>
  )
}