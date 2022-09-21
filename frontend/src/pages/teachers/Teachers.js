import UnauthorizedAccess from "../../lib/commonComponents/UnauthorisedAccess"
import CircularsSection from "../../lib/commonComponents/CircularsSection";
import ProgressSection from "./components/ProgressSection";
import AttedenceSection from "./components/AttedenceSection";
import AssignmentsSection from "./components/AssignmentsSection";

export default function Teachers({ username, privilege }) {
    if (!username || !privilege) return <UnauthorizedAccess />

    return <div>
        <CircularsSection />
        <ProgressSection username={username} />
        <AttedenceSection username={username} />
        <AssignmentsSection username={username} />
    </div>
}
