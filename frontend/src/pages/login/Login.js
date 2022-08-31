import { useState } from "react"
import { login } from "../../lib/API";
import { useNavigate } from "react-router-dom";


export default function Login({ username, setUsername, setPrivilege }) {
    const [fieldUsername, setFieldUsername] = useState(null)
    const [fieldPassword, setfieldPassword] = useState(null)

    let navigate = useNavigate();


    return (<form onSubmit={submitForm}>
        <input type="text" name="username" onChange={updateUsername} />
        <input type="password" name="password" onChange={updatePassword} />
        <button> Login</button>
    </form>)


    function updateUsername(e) {
        const value = e.target.value;
        setFieldUsername(value)
    }

    function updatePassword(e) {
        const value = e.target.value;
        setfieldPassword(value)
    }

    function submitForm(e) {
        e.preventDefault();
        login({ username: fieldUsername, password: fieldPassword, setUsername, navigate, setPrivilege })
    }
}