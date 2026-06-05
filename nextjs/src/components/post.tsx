import {Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import React from 'react'


interface IPost {
   author: string;
   title: string;
   content: string;
}

const Post = ({author, title, content}: IPost) => {
   return (

      <Card>
         <CardHeader className="card-h">
            {author}
         </CardHeader>
         <CardTitle className="card-t">
            {title}
         </CardTitle>
         <CardContent className="card-c">
            {content}
         </CardContent>
         <CardFooter className="card-f">
         </CardFooter>
      </Card>
   )
}

export default Post
   