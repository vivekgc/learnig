using CodePulse.API.Data;
using CodePulse.API.Mpodels.Domain;
using CodePulse.API.Repository.Interface;
using Microsoft.EntityFrameworkCore;

namespace CodePulse.API.Repository.Implementation
{
    public class CategoryRepository : ICategoryRepository
    {


        private readonly ApplicationDbContext dbcontext;
        public CategoryRepository(ApplicationDbContext dbContext) {
        this.dbcontext = dbContext;
        }
        public async Task<Category> CreateAsync(Category category)
        {
            await dbcontext.Categories.AddAsync(category);
            await dbcontext.SaveChangesAsync();

            return category;
        }
    }
}
