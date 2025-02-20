document.addEventListener("DOMContentLoaded", function() {
    async function fetchCourses() {
        try {
            const response = await fetch("http://127.0.0.1:8000/courses/");
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const courses = await response.json();
            displayCourses(courses);
        } catch (error) {
            console.error("Error fetching courses:", error);
            const coursesContainer = document.getElementById("courses");
            coursesContainer.innerHTML = "<p class='text-red-500'>Failed to load courses.</p>";
        }
    }

    async function displayCourses(courses) {
        const coursesContainer = document.getElementById("courses");
        coursesContainer.innerHTML = ""; // Clear existing content

        for (const course of courses) {
            const courseElement = document.createElement("div");
            courseElement.classList.add("mb-4", "p-4", "bg-white", "rounded-lg", "shadow-md");

            const courseNameElement = document.createElement("h2");
            courseNameElement.classList.add("text-xl", "font-semibold", "text-green-700", "mb-2");
            courseNameElement.textContent = course.course_title;
            courseElement.appendChild(courseNameElement);

            try {
                const lecturesResponse = await fetch(`http://127.0.0.1:8000/courses/${course.course_id}/lectures/`);
                if (!lecturesResponse.ok) {
                    throw new Error(`HTTP error! status: ${lecturesResponse.status}`);
                }
                const lectures = await lecturesResponse.json();

                const tableElement = document.createElement("table");
                tableElement.classList.add("table-auto", "w-full");

                const tableHead = document.createElement("thead");
                tableHead.classList.add("bg-green-100");
                tableHead.innerHTML = `
                    <tr>
                        <th class="px-4 py-2 text-left text-green-600">Lecture</th>
                        <th class="px-4 py-2 text-left text-green-600">Description</th>
                    </tr>
                `;
                tableElement.appendChild(tableHead);

                const tableBody = document.createElement("tbody");
                lectures.forEach(lecture => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td class="border px-4 py-2">${lecture.lecture_no}</td>
                        <td class="border px-4 py-2">${lecture.lecture_description}</td>
                    `;
                    tableBody.appendChild(row);
                });
                tableElement.appendChild(tableBody);
                courseElement.appendChild(tableElement);

            } catch (error) {
                console.error("Error fetching lectures:", error);
                courseElement.innerHTML += "<p class='text-red-500'>Failed to load lectures.</p>";
            }

            coursesContainer.appendChild(courseElement);
        }
    }

    fetchCourses();
});