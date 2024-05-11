using CodePulse.API.Data;
using CodePulse.API.Mpodels.Domain;
using CodePulse.API.Mpodels.DTO;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace CodePulse.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class BlogPostController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public BlogPostController(ApplicationDbContext _dbContext) {
            this._context = _dbContext;
        }

        //[HttpPost]
        //public async Task<IActionResult> CreateBlogPost(BlogPostRequestDto request)
        //{
        //    var category = new Category
        //    {
        //        Name = request.Name,
        //        UrlHandle = request.UrlHandle
        //    };
        //}
    }
}
