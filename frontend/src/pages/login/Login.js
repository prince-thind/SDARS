import { useState } from "react"
import { login } from "../../lib/API";
import { useNavigate } from "react-router-dom";


export default function Login({ username, setUsername, setPrivilege }) {
    const [fieldUsername, setFieldUsername] = useState(null)
    const [fieldPassword, setfieldPassword] = useState(null)

    const navigate = useNavigate();


    return (<form className="login-form form" onSubmit={submitForm}>
        <label> Enter Username
            <input type="text" name="username" required onChange={updateUsername} />
        </label>
        <label> Enter Password
            <input type="password" name="password" required onChange={updatePassword} />
        </label>
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