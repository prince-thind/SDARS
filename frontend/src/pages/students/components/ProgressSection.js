import { useEffect, useState } from "react"
import { fetchProgress } from "../../../lib/API";

export default function ProgressSection({ username }) {
    const [progress, setProgress] = useState([]);

    useEffect(() => {
        fetchProgress(username).then(subs => {
            setProgress(subs)
        })
    }, [username])


    return <section>
        <h2>Progress Report</h2>
        {progress.length === 0 ? "loading" : ""}
        <ul>
            {progress.map(e => {
                return <li key={e.id}><ProgressCard progress={e} /></li>
            })}
        </ul>
    </section>
}

function ProgressCard({ progress }) {
    return <div>
        <h3>Name:  {progress.name}</h3>
        <h4>Grade: {progress.grade}</h4>
        <p>{progress.description}</p>
    </div>
}