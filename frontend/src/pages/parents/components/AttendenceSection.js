import { useEffect, useState } from "react"
import { fetchParentsAttendence } from "../../../lib/API";

export default function Attendence({ username }) {
    const [attendence, setAttendence] = useState([]);

    useEffect(() => {
        fetchParentsAttendence(username).then(attendence => {
            setAttendence(attendence)
        })
    }, [username])


    return <section>
        <h2>Attendence</h2>
        {attendence.length === 0 ? "loading" : ""}
        <ul>
            {attendence.map(e => {
                return <li key={e.id}><AttendenceCard attendence={e} /></li>
            })}
        </ul>
    </section>
}

function AttendenceCard({ attendence }) {
    return <div>
        <h3>Total Attendence:  {attendence.attendence}</h3>
        <p> {attendence.remarks} </p>
    </div>
}