'use client'
import Link from "next/link"

export default function NavBar() {

return (
  <div className="flex flex-row space-x-4">
    <Link className="hover:text-amber-600" href="/">Home</Link>
    <Link className="hover:text-amber-600" href="/products">Products</Link>
    <Link className="hover:text-amber-600" href="/about">About</Link>
    <Link className="hover:text-amber-600" href="/contact">Contact</Link>
  </div>
)
}