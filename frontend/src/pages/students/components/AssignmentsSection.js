import { useEffect, useState } from "react"
import { fetchAssignments } from "../../../lib/API";

export default function ResultsSection() {
    const [assignments, setAssignments] = useState([]);

    useEffect(() => {
        fetchAssignments().then(tests => {
            setAssignments(tests)
        })
    }, [])


    return <section>
        <h2>Assignments</h2>
        {assignments.length === 0 ? "loading" : ""}
        <ul>
            {assignments.map(e => {
                return <li key={e.id}><Assignment assignment={e} /></li>
            })}
        </ul>
    </section>
}

function Assignment({ assignment }) {
    return <div>
        <h3> {assignment.name} ({assignment.marks} marks)</h3>
        <p>
            {assignment.description}
        </p>
        <div>Date of SUbmission{assignment.dueDate}</div>
        <a target="_blank" rel="noreferrer" href={`/students/assignments/${assignment.id}`}> Download now</a>

    </div>
}