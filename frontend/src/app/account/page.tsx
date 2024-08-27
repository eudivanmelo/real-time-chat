import { AccountPage } from "@/components/pages/account";
import { Metadata } from "next";

export const metada: Metadata = {
    title: "Perfil"
}

const Account = () => <AccountPage />;

export default Account;