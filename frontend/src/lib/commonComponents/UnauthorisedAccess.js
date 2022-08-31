import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";


export default function UnauthorizedAccess({ circular }) {
    const [time, setTime] = useState(5000);
    const navigate = useNavigate();


    useEffect(() => {
        const id = setInterval(() => {
            setTime(time => time - 1000);
        }, 1000)
        return () => clearInterval(id)
    }, [])

    useEffect(() => {
        if (time < 0) {
            navigate("/")
        }
    }, [time, navigate])

    return <div>
        unauthorized access! returing back to login in {time / 1000} seconds
    </div>
}