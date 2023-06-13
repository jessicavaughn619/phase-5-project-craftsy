'use client'
import Logout from "./components/logout";

export default function Home({ user, onSetUser }) {
    return (
        <div>
            <h1>Home Page!</h1>
            <p>Welcome, {user.username}!</p>
            <Logout onSetUser={onSetUser}/>
        </div>
    )

}