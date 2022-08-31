import { useEffect, useState } from "react"
import { fetchCirculars } from "../../lib/API";
import Circular from "../../lib/commonComponents/Circular";
import UnauthorizedAccess from "../../lib/commonComponents/UnauthorisedAccess";

export default function Students({ username, privilege }) {

    const [circulars, setCirculars] = useState([]);

    useEffect(() => {
        fetchCirculars().then(circulars => {
            setCirculars(circulars)
        })
    }, [])



    if (!username || !privilege) return <UnauthorizedAccess />


    return <div>
        <h2>Studnets's page </h2>
        <section>
            <h2>Circulars</h2>
            {circulars.length === 0 ? "loading" : ""}
            <ul>
                {circulars.map(e => {
                    return <li><Circular circular={e} /></li>
                })}
            </ul>
        </section>

    </div>


}