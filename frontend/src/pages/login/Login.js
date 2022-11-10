import { useState } from "react"
import { login } from "../../lib/API";
import { useNavigate } from "react-router-dom";
import Error from "../../lib/commonComponents/ErrorToast";


export default function Login({ username, setUsername, setPrivilege, setUserClass }) {
    const [fieldUsername, setFieldUsername] = useState(null)
    const [fieldPassword, setfieldPassword] = useState(null)
    const [error,setError]=useState(null)

    const navigate = useNavigate();


    return (<form className="login-form" onSubmit={submitForm}>
        <label> Enter Username
            <input type="text" name="username" required onChange={updateUsername} />
        </label>
        <label> Enter Password
            <input type="password" name="password" required onChange={updatePassword} />
        </label>
        <button> Login</button>
        {error && <Error error={error} />}
    </form>)


    function updateUsername(e) {
        const value = e.target.value;
        setFieldUsername(value)
    }

    function updatePassword(e) {
        const value = e.target.value;
        setfieldPassword(value)
    }

   async function submitForm(e) {
        e.preventDefault();
        const {error}= await login({ username: fieldUsername, password: fieldPassword, setUsername, navigate, setPrivilege, setUserClass })
        if(error){
            setError(error)
        }
    }
}