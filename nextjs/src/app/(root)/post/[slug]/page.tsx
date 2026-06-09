import { Post, IPost } from "@/components/post"
import { posts } from "@/components/posts"
import Link from "next/link"
import "@/app/(root)/root.css"

interface PostPageProps {
  params: Promise<{
    slug: string
  }>
}

export default async function PostPage({ params }: PostPageProps) {
  const { slug } = await params
  const post = posts.find((p: IPost) => p.slug === slug)

  if (!post) {
    return (
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold mb-4">Post not found</h1>
        <Link href="/" className="text-blue-500 hover:underline">
          Back to Home
        </Link>
      </div>
    )
  }

  return (
    <div className="container mx-auto p-4">
      <Link href="/" className="text-blue-500 hover:underline mb-4 inline-block">
        ← Back to Posts
      </Link>
      <div className="mt-6">
        <Post
          id={post.id}
          slug={post.slug}
          pro_pic={post.pro_pic}
          author={post.author}
          title={post.title}
          content={post.content}
        />
      </div>
    </div>
  )
}
