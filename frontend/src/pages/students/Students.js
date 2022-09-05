import CircularsSection from "../../lib/commonComponents/CircularsSection";
import ResultsSection from "./components/ResultsSection"
import AssignmentsSection from "./components/AssignmentsSection"
import UnauthorizedAccess from "../../lib/commonComponents/UnauthorisedAccess";
import Attendence from "./components/AttedenceSection";
import ProgressSection from "./components/ProgressSection";

export default function Students({ username, privilege }) {
    if (!username || !privilege) return <UnauthorizedAccess />

    return <div>
        <h2>Studnets's page </h2>
        <CircularsSection />
        <ResultsSection username={username} />
        <AssignmentsSection />
        <ProgressSection username={username} />
        <Attendence username={username} />

    </div>


}