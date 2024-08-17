import { handleSignOut } from "@/lib/server/auth"
import { useAuthStore } from "@/stores/authStore"
import { useChatStore } from "@/stores/chatStore"
import { useTheme } from "next-themes"
import { usePathname } from "next/navigation"
import { toast } from "sonner"

export const Header = () => {
    const { setTheme } = useTheme()
    const { user, clearUser } = useAuthStore()
    const { setChat, showChatsList, setShowChatsList } = useChatStore()

    const pathname = usePathname()

    const handleLogout = () => {
        handleSignOut()
        setChat(null)
        clearUser()
        toast.success('Deslogado com sucesso!', { position: "top-center" })
    }

    return (
        <header className="h-header px-2 bg-slate-100 dark:bg-slate-900 border-slate-50 dark:border-slate-800">
            <nav>
                
            </nav>
        </header>
    )
}