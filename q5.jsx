import {useState, useEffect} from 'react';
function UserList({ list }) {
  const [selectedUser, setSelectedUser] = useState(null);
  useEffect(() => {
    if (selectedUser) {
      console.log('Selected:', selectedUser.name);
    }
  }, [selectedUser]);
  return (
    <div>
      {list?.map(user => (
        <div key={user.id} onClick={() => setSelectedUser(user)}>
          {user.name}
        </div>
      ))}
      <button onClick={() => setSelectedUser(null)}>Clear</button>
    </div>
  );
}
export default UserList;
