import React from "react";

export default function NavBar({ user, onSetUser }) {
    function handleLogoutClick() {
        fetch("/api/logout", { method: "DELETE" }).then((r) => {
            if (r.ok) {
              onSetUser(null);
            }
          });
        }
return (
  <div id="navbar-container-wrapper">
    <h1>Craftsy</h1>
    <p id="welcome">Welcome, {user.username}!</p>
    <div id="links">
      <button onClick={handleLogoutClick}>Logout</button>
    </div>
  </div>
)
}