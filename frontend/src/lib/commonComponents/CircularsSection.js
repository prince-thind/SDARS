import { useEffect, useState } from "react"
import { fetchCirculars } from "../API";

export default function CircularsSection() {
    const [circulars, setCirculars] = useState([]);

    useEffect(() => {
        fetchCirculars().then(circulars => {
            setCirculars(circulars)
        })
    }, [])


    return <section className="module">
        <h3>Circulars</h3>
        {circulars.length === 0 ? "loading" : ""}
        <ul>
            {circulars.map(e => {
                return <li key={e.id}><Circular circular={e} /></li>
            })}
        </ul>
    </section>
}

function Circular({ circular }) {
    return <div className="module-item">
        <h4> {circular.name} - ({formatDate(circular.date)})</h4>
        <p> {circular.description}</p>
    </div>
}

function formatDate(date){
    const newDate=new Date(date);
    const formattedDate=newDate.toLocaleDateString();
    return formattedDate
}