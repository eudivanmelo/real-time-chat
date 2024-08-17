import { User } from "@/types/user"
import { create } from "zustand"

export type AuthState = {
    user: User | null
}

export type AuthActions = {
    setUser: (user: User) => void,
    clearUser: () => void
}

export type AuthStore = AuthState & AuthActions

export const userAuthStore = create<AuthStore>((set) => ({
    user: null,
    setUser: (user) => set({ user }),
    clearUser: () => set({ user: null })
}))