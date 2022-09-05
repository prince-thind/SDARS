import CircularsSection from "../../lib/commonComponents/CircularsSection";
import ResultsSection from "./components/ResultsSection"
import UnauthorizedAccess from "../../lib/commonComponents/UnauthorisedAccess";

export default function Students({ username, privilege }) {
    if (!username || !privilege) return <UnauthorizedAccess />

    return <div>
        <h2>Studnets's page </h2>
        <CircularsSection />
        <ResultsSection username={username} />

    </div>


}