import {Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import React from 'react'
import Image from "next/image"


export interface IPost {
   id: string;
   slug: string;
   pro_pic: string;
   author: string;
   title: string;
   content: string;
}

export const Post = ({id, slug, pro_pic, author, title, content}: IPost) => {
   return (

      <Card >
         <div className="flex items-center gap-6">
            <Image src={pro_pic} alt="default image" width={45} height={45} className="img" />
            <CardHeader >
               <h2>{author}</h2>
            </CardHeader>
         </div>
         <CardTitle >
            {title}
         </CardTitle>
         <CardContent >
            {content}
         </CardContent>
      </Card>
   )
}
