import {Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import React from 'react'
import Image from "next/image"
import { formatDate } from "@/lib/utils";



interface Author {
   id: number;
   username: string;
   image_url: string | null;
}


export interface IPost {
   id: number;
   slug: string;
   title: string;
   content: string;
   date_posted: string;
   author: Author;

}


export const Post = ({id, title, content, date_posted, author}: IPost) => {
   return (
      <Card key={id as unknown as string} className="post-card" >
         <div className="flex items-center gap-6 mb-4">
            {author.image_url && <Image src={author.image_url} alt={author.username || 'author'} width={45} height={45} className="img rounded-full" unoptimized />}
            <div>
               <h2 className="font-semibold">{author.username}</h2>
               <p className="text-sm text-gray-500">{formatDate(date_posted)}</p>
            </div>
         </div>
         <CardTitle className="mb-3">
            {title}
         </CardTitle>
         <CardContent >
            {content}
         </CardContent>
      </Card>
   )
}
