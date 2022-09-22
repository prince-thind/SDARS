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
        <div>
            <h4> {assignment.name} - ({assignment.maxMarks} marks)</h4>
            <p>
                {assignment.description}
            </p>
            <h5>Submission by: {new Date(assignment.dueDate).toLocaleDateString()}</h5>
        </div>
        <button onClick={download}> Download now</button>

    </div>

    function download() {
        const filename = 'assignment' + assignment.id + '.txt';
        const text=assignment.text;

        const element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        element.setAttribute('download', filename);

        element.style.display = 'none';
        document.body.appendChild(element);

        element.click();

        document.body.removeChild(element);
    }
}