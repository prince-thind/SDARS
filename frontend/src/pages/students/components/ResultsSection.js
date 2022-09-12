import { useEffect, useState } from "react"
import { fetchResults } from "../../../lib/API";

export default function ResultsSection({ username }) {
    const [results, setResults] = useState([]);

    useEffect(() => {
        fetchResults(username).then(tests => {
            setResults(tests)
        })
    }, [username])


    return <section className="module result-module">
        <h3>Results</h3>
        {results.length === 0 ? "loading" : ""}
        <ul>
            {results.map(e => {
                return <li key={e.id}><Test test={e} /></li>
            })}
        </ul>
    </section>
}

function Test({ test }) {
    return <div className="module-item">
        <h4> {test.name} ({test.type})</h4>
        <div className="marks">
            <span> {test.marksGot}</span>
            <span> / </span>
            <span>{test.maxMarks}</span></div>
    </div>
}