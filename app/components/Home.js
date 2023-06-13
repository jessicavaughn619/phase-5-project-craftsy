'use client'
import NavBar from "./NavBar";

export default function Home({ user, onSetUser }) {
    return (
        <div>
            <h1>Home Page!</h1>
            <NavBar user={user} onSetUser={onSetUser}/>
        </div>
    )

}