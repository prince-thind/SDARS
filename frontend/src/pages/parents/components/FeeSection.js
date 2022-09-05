import { useEffect, useState } from "react"
import { fetchFees } from "../../../lib/API";

export default function FeeSection({ username }) {
    const [fees, setFees] = useState([]);

    useEffect(() => {
        fetchFees(username).then(e => {
            setFees(e)
        })
    }, [username])


    return <section>
        <h2>Progress Report</h2>
        {fees.length === 0 ? "loading" : ""}
        <ul>
            {fees.map(e => {
                return <li key={e.id}><FeeCard feeElement={e} /></li>
            })}
        </ul>
    </section>
}

function FeeCard({ feeElement }) {
    return <div>
        <h3>Name:  {feeElement.name}</h3>
        <h4>Cost: {feeElement.cost}</h4>
        <p>{feeElement.description}</p>
    </div>
}