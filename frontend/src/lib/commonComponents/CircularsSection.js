import { useEffect, useState } from "react"
import { fetchCirculars } from "../API";

export default function CircularsSection() {
    const [circulars, setCirculars] = useState([]);

    useEffect(() => {
        fetchCirculars().then(circulars => {
            setCirculars(circulars)
        })
    }, [])

    
    return <section>
        <h2>Circulars</h2>
        {circulars.length === 0 ? "loading" : ""}
        <ul>
            {circulars.map(e => {
                return <li key={e.id}><Circular circular={e} /></li>
            })}
        </ul>
    </section>
}

function Circular({ circular }) {
    return <div>
        <h3> {circular.name}</h3>
        <p> {circular.description}</p>
        <h3> {circular.date}</h3>
    </div>
}