import {useEffect, useState} from "react";
export default function UserSearch() {
  const [search, setSearch] = useState("");
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  useEffect(() => {
    if (!search.trim()) return setUsers([]);
    const controller = new AbortController();
    const timer = setTimeout(async () => {
      setLoading(true);
      setError("");
      try {
        const res = await fetch(
          `/api/users?search=${encodeURIComponent(search)}`,
          { signal: controller.signal }
        );
        if (!res.ok) throw new Error();
        setUsers(await res.json());
      } catch (e) {
        if (e.name !== "AbortError") setError("Something went wrong");
      } finally {
        setLoading(false);
      }
    }, 300);
    return () => {
      clearTimeout(timer);
      controller.abort();
    };
  }, [search]);
  return (
    <div>
      <h2>User Search</h2>
      <input
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search users..."
      />
      {loading && <p>Loading...</p>}
      {error && <p>{error}</p>}
      {!loading && !error && search && !users.length && <p>No users found</p>}
      {users.map((user) => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  );
}