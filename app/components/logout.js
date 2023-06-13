'use client'

export default function Logout({ onSetUser }) {
    function handleLogoutClick() {
        fetch("/api/logout", { method: "DELETE" }).then((r) => {
            if (r.ok) {
              onSetUser(null);
            }
          });
        }
return (
  <div id="logout-container-wrapper">
      <button className="hover:text-amber-700" onClick={handleLogoutClick}>Logout</button>
  </div>
)
}