"use client";

import { z } from 'zod'

/* Sign In */
export const signInSchema = z.object({
    email: z.string().email({message: 'Email inválido'}),
    password: z.string().min(1, {message: 'Senha é obrigatória'})
})

export type SignInData = z.infer<typeof signInSchema>

/* Sign Up */
export const signUpSchema = z.object({
    name: z.string().min(1, {message: 'Nome é obrigatório'}).max(80, {message: 'Nome deve ter no máximo 80 caracteres'}),
    email: z.string().email({message: 'Email inválido'}).max(254, {message: 'Email deve ter no máximo 254 caracteres'}),
    password: z.string()
               .min(1, {message: 'Senha é obrigatória'})
               .regex(/^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9\s]).+$/, 
                      {message: 'Senha deve conter pelo menos 1 letra, 1 número e 1 caractere especial'})
               .max(80, {message: 'Senha deve ter no máximo 80 caracteres'}),
})

export type SingUpData = z.infer<typeof signUpSchema>