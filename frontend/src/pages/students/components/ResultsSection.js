import { useEffect, useState } from "react"
import { fetchResults } from "../../../lib/API";

export default function ResultsSection() {
    const [results, setResults] = useState([]);

    useEffect(() => {
        fetchResults().then(tests => {
            setResults(tests)
        })
    }, [])


    return <section>
        <h2>Results</h2>
        {results.length === 0 ? "loading" : ""}
        <ul>
            {results.map(e => {
                return <li key={e.id}><Test test={e} /></li>
            })}
        </ul>
    </section>
}

function Test({ test }) {
    return <div>
        <h3> {test.name} ({test.type})</h3> 
        <div>
            <span> {test.marksGot}</span>
            <span>/</span>
            <span> {test.maxMarks}</span></div>
    </div>
}