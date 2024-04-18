using CodePulse.API.Mpodels.Domain;

namespace CodePulse.API.Repository.Interface
{
    public interface ICategoryRepository
    {

        Task<Category> CreateAsync(Category category);
    }
}
