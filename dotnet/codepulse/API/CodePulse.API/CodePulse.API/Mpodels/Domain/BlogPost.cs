namespace CodePulse.API.Mpodels.Domain
{
    public class BlogPost
    {
        public Guid Id { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }

        public string Content { get; set; }

        public string FeauturedImageUrl { get; set; }

        public string UrlHandle { get; set; }


        public DateTime PublishedDate { get; set; }

        public string Author { get; set; }

        public bool IsVisible { get; set; }

    }
}
