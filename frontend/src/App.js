import { HashRouter, Routes, Route } from 'react-router-dom'
import Parents from './pages/parents/Parents';
import Teachers from './pages/teachers/Teachers';
import Students from './pages/students/Students';
import Login from './pages/login/Login';
import { useState } from 'react';
import Layout from './lib/commonComponents/Layout';

function App() {
  const [username, setUsername] = useState(null);
  const [userClass, setUserClass] = useState(null);
  const [privilege, setPrivilege] = useState(null);

  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path="login" element={<Login username={username} setUsername={setUsername} setPrivilege={setPrivilege} setUserClass={setUserClass}/>} />
          <Route index element={<Login username={username} setUsername={setUsername} setPrivilege={setPrivilege} setUserClass={setUserClass} />} />
          <Route path="students" element={<Students username={username} privilege={privilege} userClass={userClass} />} />
          <Route path="parents" element={<Parents username={username} privilege={privilege} />} />
          <Route path="teachers" element={<Teachers username={username} privilege={privilege}/>} />
        </Route>
      </Routes>
    </HashRouter>
  );
}

export default App;
