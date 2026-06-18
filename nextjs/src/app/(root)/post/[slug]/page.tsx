

import Link from "next/link"
import "@/app/(root)/root.css"
import {IPost, Post} from "@/components/post"

interface PostPageProps {
  params: {
    slug: string
  }
}


export default async function PostPage({ params }: PostPageProps) {

  const res_para = await params
  const { slug } = res_para  
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/posts/${slug}`)
  if (!res.ok) throw new Error('Post not found')
  const post: IPost = await res.json()
  console.log(post)

  return (
    <div className="container mx-auto p-4">
      <Link href="/" className="text-blue-500 hover:underline mb-4 inline-block">
        ← Back to Posts
      </Link>
      <li key={post.id}>
        <Link href={`/post/${post.slug}`} className="no-underline">
          <Post {...post} />
        </Link>
    </li>
    </div>
  )
}
