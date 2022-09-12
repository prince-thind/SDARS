import { useEffect, useState } from "react"
import { fetchAssignments } from "../../../lib/API";

export default function ResultsSection() {
    const [assignments, setAssignments] = useState([]);

    useEffect(() => {
        fetchAssignments().then(tests => {
            setAssignments(tests)
        })
    }, [])


    return <section className="module">
        <h3>Assignments</h3>
        {assignments.length === 0 ? "loading" : ""}
        <ul>
            {assignments.map(e => {
                return <li key={e.id}><Assignment assignment={e} /></li>
            })}
        </ul>
    </section>
}

function Assignment({ assignment }) {
    return <div className="module-item assignments-module-item">
        <h4> {assignment.name} - ({assignment.maxMarks} marks)</h4>
        <p>
            {assignment.description}
        </p>
        <h5>Submission by: {new Date(assignment.dueDate).toLocaleDateString()}</h5>
        <a target="_blank" rel="noreferrer" href={`/students/assignments/${assignment.id}`}> Download now</a>

    </div>
}